import Link from "next/link";
import "./page.css";

export default function Home() {
  return (
    <div className="home-container animate-fade-in">
      <div className="hero-section glass-panel">
        <h1 className="hero-title">
          Master <span className="highlight">GenAI</span> & <span className="highlight">Machine Learning</span>
        </h1>
        <p className="hero-subtitle">
          The ultimate platform to practice coding challenges, build intuition, 
          and prepare for top-tier AI engineering roles. 
          Write algorithms, not just prompts.
        </p>
        
        <div className="hero-actions">
          <Link href="/problems" className="hero-btn-primary">
            Start Coding Now
          </Link>
          <a href="#features" className="hero-btn-secondary">
            Explore Features
          </a>
        </div>
      </div>
      
      <div className="features-grid" id="features">
        <div className="feature-card glass-panel">
          <h3>🧠 Neural Architectures</h3>
          <p>Implement Transformers, CNNs, and complete ML pipelines from scratch in our in-browser IDE.</p>
        </div>
        <div className="feature-card glass-panel">
          <h3>⚡ Instant Evaluation</h3>
          <p>Get real-time feedback on your model's accuracy, performance, and memory usage.</p>
        </div>
        <div className="feature-card glass-panel">
          <h3>📊 Global Leaderboard</h3>
          <p>Compete with AI engineers globally. Compare efficient solutions and learn from top performers.</p>
        </div>
      </div>
    </div>
  );
}
