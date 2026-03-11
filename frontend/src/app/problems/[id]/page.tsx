"use client";

import { useEffect, useState, use } from 'react';
import { useRouter } from 'next/navigation';
import Editor from '@monaco-editor/react';
import './problem-detail.css';

interface Problem {
  id: string;
  title: string;
  difficulty: string;
  description: string;
  starting_code: string;
}

interface ExecResult {
  status: string;
  output: string;
  execution_time_ms: number;
}

export default function ProblemDetail({ params }: { params: Promise<{ id: string }> }) {
  const router = useRouter();
  const { id } = use(params);
  const [problem, setProblem] = useState<Problem | null>(null);
  const [code, setCode] = useState<string>('');
  const [running, setRunning] = useState(false);
  const [result, setResult] = useState<ExecResult | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
    fetch(`${apiUrl}/api/problems/${id}`)
      .then(res => {
        if (!res.ok) throw new Error('Not found');
        return res.json();
      })
      .then(data => {
        setProblem(data);
        setCode(data.starting_code);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        router.push('/problems');
      });
  }, [id, router]);

  const handleRun = async () => {
    setRunning(true);
    setResult(null);
    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const res = await fetch(`${apiUrl}/api/execute`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code, problem_id: id })
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
      setResult({ status: 'error', output: 'Network error or server down', execution_time_ms: 0 });
    }
    setRunning(false);
  };

  if (loading) return <div className="loading-state">Loading problem...</div>;
  if (!problem) return null;

  return (
    <div className="problem-detail-container">
      <div className="problem-description-panel glass-panel">
        <h1 className="problem-title">{problem.title}</h1>
        <div className={`problem-difficulty diff-${problem.difficulty.toLowerCase()}`}>
          {problem.difficulty}
        </div>
        
        <div className="problem-body">
          <div dangerouslySetInnerHTML={{ __html: problem.description }} />
        </div>
        
        {result && (
          <div className={`execution-result ${result.status}`}>
            <h3>Execution {result.status === 'pass' ? 'Success' : 'Failed'} ({result.execution_time_ms.toFixed(2)} ms)</h3>
            <pre className="output-console">{result.output}</pre>
          </div>
        )}
      </div>
      
      <div className="editor-panel glass-panel">
        <div className="editor-header">
          <span className="lang-badge">Python 3</span>
          <div className="editor-actions">
            <button 
              className="btn-primary" 
              onClick={handleRun}
              disabled={running}
            >
              {running ? 'Running...' : 'Run Code'}
            </button>
          </div>
        </div>
        
        <div className="editor-container">
          <Editor
            height="100%"
            defaultLanguage="python"
            theme="vs-dark"
            value={code}
            onChange={(val) => setCode(val || '')}
            options={{
              minimap: { enabled: false },
              fontSize: 14,
              fontFamily: "'Fira Code', 'Menlo', 'Monaco', 'Courier New', monospace",
              padding: { top: 16 },
              scrollBeyondLastLine: false,
              roundedSelection: false,
              scrollbar: {
                vertical: 'visible',
                horizontal: 'visible',
              }
            }}
          />
        </div>
      </div>
    </div>
  );
}
