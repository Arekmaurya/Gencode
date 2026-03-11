import Link from 'next/link';
import './Navbar.css';

export default function Navbar() {
  return (
    <nav className="navbar glass-panel">
      <div className="nav-brand">
        <Link href="/">
          <span className="brand-icon">✨</span>
          <span className="brand-text">GenCode</span>
        </Link>
      </div>
      <div className="nav-links">
        <Link href="/problems" className="nav-link">Problems</Link>
        <Link href="/leaderboard" className="nav-link">Leaderboard</Link>
      </div>
      <div className="nav-actions">
        <button className="btn-secondary">Sign In</button>
        <button className="btn-primary">Register</button>
      </div>
    </nav>
  );
}
