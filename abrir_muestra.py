from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
import argparse, os, re, webbrowser

class MediaHandler(SimpleHTTPRequestHandler):
    """Serve local files with byte ranges so browsers can seek within MP4s."""
    def send_head(self):
        self.byte_count = None
        path = Path(self.translate_path(self.path))
        requested = self.headers.get('Range')
        if not requested or not path.is_file():
            return super().send_head()
        size = path.stat().st_size
        match = re.fullmatch(r'bytes=(\d*)-(\d*)', requested.strip())
        if not match or not any(match.groups()):
            self.send_error(416, 'Invalid byte range')
            return None
        left,right = match.groups()
        start = int(left) if left else max(0,size-int(right))
        end = min(size-1,int(right)) if left and right else size-1
        if start >= size or start > end:
            self.send_response(416)
            self.send_header('Content-Range', f'bytes */{size}')
            self.send_header('Content-Length','0')
            self.end_headers()
            return None
        stream = path.open('rb')
        stream.seek(start)
        self.byte_count = end-start+1
        self.send_response(206)
        self.send_header('Content-type', self.guess_type(str(path)))
        self.send_header('Accept-Ranges','bytes')
        self.send_header('Content-Range',f'bytes {start}-{end}/{size}')
        self.send_header('Content-Length',str(self.byte_count))
        self.end_headers()
        return stream

    def copyfile(self, source, outputfile):
        try:
            if self.byte_count is None:
                return super().copyfile(source,outputfile)
            remaining = self.byte_count
            while remaining:
                block=source.read(min(65536,remaining))
                if not block: break
                outputfile.write(block)
                remaining-=len(block)
        except (BrokenPipeError,ConnectionResetError):
            pass

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--port',type=int,default=0)
    parser.add_argument('--no-browser',action='store_true')
    args=parser.parse_args()
    root=Path(__file__).resolve().parent/'dist'
    server=ThreadingHTTPServer(('127.0.0.1',args.port),partial(MediaHandler,directory=str(root)))
    url=f'http://127.0.0.1:{server.server_port}/'
    print(f'Bilbobus · Muestra local\n{url}\nMantén esta ventana abierta. Para finalizar pulsa Ctrl+C.',flush=True)
    if not args.no_browser: webbrowser.open(url)
    try: server.serve_forever()
    except KeyboardInterrupt: server.server_close()
