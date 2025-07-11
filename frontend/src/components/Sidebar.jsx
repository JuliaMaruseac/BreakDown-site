import { Link } from 'react-router-dom';

export default function Sidebar() {
  return (
    <nav className="w-48 bg-[#15132b] p-4 space-y-4">
      <h1 className="text-xl text-purple-400">BreakDown</h1>
      <ul className="space-y-2">
        <li><Link to="/">Dashboard</Link></li>
        <li><Link to="/cases">Cases</Link></li>
        <li><Link to="/new">New Case</Link></li>
      </ul>
    </nav>
  );
}
