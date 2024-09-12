import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Item } from './types';

const App: React.FC = () => {
  const [item, setItem] = useState<Item | null>(null);
  const [error, setError] = useState<string | null>(null);
  const itemId = 1;  // 取得するアイテムのIDを指定

  useEffect(() => {
    axios.get<Item>(`http://localhost:8000/items/${itemId}`)
      .then(response => {
        setItem(response.data);
      })
      .catch(error => {
        setError('There was an error fetching the data!');
        console.error('There was an error fetching the data!', error);
      });
  }, [itemId]);

  return (
    <div>
      <h1>Item 詳細</h1>
      {error && <p>{error}</p>}
      {item ? (
        <div>
          <h2>ID: {item.id}</h2>
          <p>Detail: {item.detail}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default App;
