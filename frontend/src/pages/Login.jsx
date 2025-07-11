import { useState } from 'react';
import { useAuth } from '../context/AuthContext';

export default function Login() {
  const { login } = useAuth();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = e => {
    e.preventDefault();
    login(username);
  };

  return (
    <form onSubmit={handleSubmit} className="m-auto w-64 p-4 bg-[#15132b] text-white space-y-4">
      <div>
        <label className="block">Username</label>
        <input value={username} onChange={e => setUsername(e.target.value)} className="w-full text-black" />
      </div>
      <div>
        <label className="block">Password</label>
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} className="w-full text-black" />
      </div>
      <button type="submit" className="px-4 py-2 bg-purple-600">Login</button>
    </form>
  );
}
