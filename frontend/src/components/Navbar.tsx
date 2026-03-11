"use client";

import Link from 'next/link';
import { useAuth } from '@/context/AuthContext';
import './Navbar.css';

export default function Navbar() {
  const { user, logout } = useAuth();

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
        {user ? (
          <div className="user-info">
            <span className="username">Hi, {user.username}</span>
            <button className="btn-secondary" onClick={logout}>Sign Out</button>
          </div>
        ) : (
          <>
            <Link href="/login">
              <button className="btn-secondary">Sign In</button>
            </Link>
            <Link href="/register">
              <button className="btn-primary">Register</button>
            </Link>
          </>
        )}
      </div>
    </nav>
  );
}
