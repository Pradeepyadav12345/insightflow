const appStats = [
  { label: 'Datasets', value: '128', delta: '+14%' },
  { label: 'Analyses', value: '2.4k', delta: '+8.2%' },
  { label: 'Insights', value: '89', delta: '+11%' },
  { label: 'Alerts', value: '12', delta: '-2' },
];

const segmentPerformance = [
  { name: 'Enterprise', value: 82, trend: '+12.4%' },
  { name: 'Mid-market', value: 68, trend: '+7.1%' },
  { name: 'SMB', value: 54, trend: '+3.8%' },
  { name: 'Retail', value: 44, trend: '-1.6%' },
];

const recentReports = [
  { name: 'Q3 Revenue Summary', owner: 'Finance Ops', time: '2h ago' },
  { name: 'Customer Retention Review', owner: 'Growth', time: '5h ago' },
  { name: 'Product Adoption Analysis', owner: 'Product', time: 'Yesterday' },
];

export default function App() {
  return (
    <main className="app-shell">
      <div className="glass-panel hero-panel">
        <div className="badge-row">
          <span className="badge">InsightFlow AI</span>
          <span className="status-pill">Live workspace</span>
        </div>
        <h1>Ask your data. Get analysis, insights, visualizations and reports.</h1>
        <p>
          Enterprise AI data analysis platform designed for secure natural-language exploration,
          reporting, forecasting, and decision support.
        </p>
        <div className="actions">
          <button className="primary">Open chat</button>
          <button className="secondary">Upload dataset</button>
        </div>
      </div>

      <section className="stats-grid">
        {appStats.map((stat) => (
          <article key={stat.label} className="glass-panel stat-card">
            <div className="stat-label">{stat.label}</div>
            <div className="stat-value">{stat.value}</div>
            <div className="stat-delta">{stat.delta}</div>
          </article>
        ))}
      </section>

      <section className="content-grid">
        <div className="glass-panel content-panel large-panel">
          <div className="panel-header">
            <h2>Business overview</h2>
            <span>Last 30 days</span>
          </div>
          <div className="body-grid">
            <div className="chart-placeholder" aria-label="Revenue chart representation">
              <div className="bar" style={{ height: '45%' }} />
              <div className="bar" style={{ height: '65%' }} />
              <div className="bar" style={{ height: '74%' }} />
              <div className="bar" style={{ height: '58%' }} />
              <div className="bar" style={{ height: '82%' }} />
              <div className="bar" style={{ height: '90%' }} />
            </div>
            <ul className="insight-list">
              <li><strong>Revenue trend</strong>: Up 14.2% versus prior period.</li>
              <li><strong>Top segment</strong>: Enterprise accounts contributed 41% of total revenue.</li>
              <li><strong>Recommendation</strong>: Increase pricing in the North region after validating margin pressure.</li>
            </ul>
          </div>
        </div>

        <aside className="glass-panel content-panel side-panel">
          <div className="panel-header">
            <h2>Segment health</h2>
          </div>
          <div className="segment-list">
            {segmentPerformance.map((segment) => (
              <div key={segment.name} className="segment-row">
                <div className="segment-meta">
                  <span>{segment.name}</span>
                  <small>{segment.trend}</small>
                </div>
                <div className="segment-meter">
                  <span style={{ width: `${segment.value}%` }} />
                </div>
              </div>
            ))}
          </div>
        </aside>
      </section>

      <section className="glass-panel content-panel bottom-panel">
        <div className="panel-header">
          <h2>Recent reports</h2>
          <button className="secondary compact">View all</button>
        </div>
        <div className="report-list">
          {recentReports.map((report) => (
            <div key={report.name} className="report-item">
              <div>
                <div className="report-name">{report.name}</div>
                <div className="report-owner">{report.owner}</div>
              </div>
              <span className="report-time">{report.time}</span>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}
