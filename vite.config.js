import {defineConfig} from 'vite';
import react from '@vitejs/plugin-react';
export default defineConfig({base:'./',plugins:[react(),{name:'local-demo-session',configureServer(server){server.middlewares.use('/api/session',(req,res)=>{res.setHeader('Content-Type','application/json');res.end(JSON.stringify({mode:'demo',user:{id:'local-demo',username:'admin-demo',role:'admin',expiresAt:null,active:true}}));});}}]});
