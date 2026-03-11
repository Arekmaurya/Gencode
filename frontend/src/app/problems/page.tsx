"use client";

import { useEffect, useState } from 'react';
import Link from 'next/link';
import './problems.css';

interface Problem {
  id: string;
  title: string;
  difficulty: string;
  description: string;
}

export default function ProblemsPage() {
  const [problems, setProblems] = useState<Problem[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch mock problems from our FastAPI backend
    const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
    fetch(`${apiUrl}/api/problems`)
      .then(res => res.json())
      .then(data => {
        setProblems(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Failed to fetch problems', err);
        setLoading(false);
      });
  }, []);

  return (
    <div className="problems-container animate-fade-in">
      <h1 className="page-title">GenAI & ML Problems</h1>
      <p className="page-subtitle">Practice real-world AI engineering challenges.</p>
      
      <div className="problems-list glass-panel">
        <div className="list-header">
          <div className="col-title">Title</div>
          <div className="col-difficulty">Difficulty</div>
          <div className="col-status">Status</div>
        </div>
        
        {loading ? (
          <div className="loading-state">Loading problems...</div>
        ) : (
          problems.map((problem) => (
            <Link href={`/problems/${problem.id}`} key={problem.id} className="problem-row">
              <div className="col-title">{problem.title}</div>
              <div className={`col-difficulty diff-${problem.difficulty.toLowerCase()}`}>
                {problem.difficulty}
              </div>
              <div className="col-status">Todo</div>
            </Link>
          ))
        )}
      </div>
    </div>
  );
}
