import React from 'react';
import {createRoot} from 'react-dom/client';
import Bilbobus from './Bilbobus.jsx';
import {AccessGate} from './BilbobusAccess.jsx';
import 'maplibre-gl/dist/maplibre-gl.css';
import './bilbobus.css';
createRoot(document.getElementById('root')).render(<AccessGate>{(session,logout)=><Bilbobus key={session.user.id} session={session} logout={logout}/>}</AccessGate>);
