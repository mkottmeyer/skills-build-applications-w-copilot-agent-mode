
import React, { useEffect, useState } from 'react';

const API = 'http://localhost:8000/api/';

function ResourceList({ resource }) {
  const [data, setData] = useState([]);
  useEffect(() => {
    fetch(API + resource + '/')
      .then(res => res.json())
      .then(json => setData(json.results || json))
      .catch(() => setData([]));
  }, [resource]);
  return (
    <div>
      <h2>{resource.charAt(0).toUpperCase() + resource.slice(1)}</h2>
      <pre style={{textAlign: 'left', background: '#f4f4f4', padding: '1em'}}>
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
}

function App() {
  const [tab, setTab] = useState('users');
  const resources = ['users', 'teams', 'activities', 'workouts', 'leaderboard'];
  return (
    <div className="App">
      <h1>OctoFit Tracker Demo</h1>
      <nav style={{marginBottom: '1em'}}>
        {resources.map(r => (
          <button key={r} onClick={() => setTab(r)} style={{marginRight: 8, fontWeight: tab === r ? 'bold' : 'normal'}}>{r}</button>
        ))}
      </nav>
      <ResourceList resource={tab} />
    </div>
  );
}

export default App;
