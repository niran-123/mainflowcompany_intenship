import React, { useState } from 'react';

function Greeting({ name }) {
  const [count, setCount] = useState(0);

  return (
    <div className="p-4 border rounded-lg shadow-md max-w-sm mx-auto text-center">
      <h1 className="text-xl font-bold mb-2">Hello, {name}!</h1>
      <p className="text-gray-700">You have clicked {count} times.</p>
      <button 
        onClick={() => setCount(count + 1)}
        className="mt-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">
        Click Me
      </button>
    </div>
  );
}

export default function App() {
  return (
    <div className="h-screen flex justify-center items-center bg-gray-100">
      <Greeting name="React Learner" />
    </div>
  );
}
