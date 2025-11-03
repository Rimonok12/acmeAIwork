export default function ResultCard({ item }) {
  return (
    <article className="card">
      <header className="cardHeader">
        <h2>{item.title}</h2>
        <span className="score">{Math.round(item.score * 100)}%</span>
      </header>
      <p>{item.summary}</p>
    </article>
  );
}
