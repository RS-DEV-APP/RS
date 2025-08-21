import React from 'react'
import { createRoot } from 'react-dom/client'

function App() {
  return (
    <div style={{padding: 24, fontFamily: 'Inter, ui-sans-serif, system-ui'}}>
      <h1>Broadcast Rights & Scheduling</h1>
      <p>API: <a href="http://localhost:8000/docs" target="_blank">OpenAPI Docs</a></p>
      <ul>
        <li><a href="#" onClick={async (e) => { e.preventDefault(); const r = await fetch('/api/health'); alert(JSON.stringify(await r.json())); }}>Ping API</a></li>
      </ul>
    </div>
  )
}

const root = createRoot(document.getElementById('root')!)
root.render(<App />)
