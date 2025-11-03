import ResultCard from './ResultCard';

export default function ResultsList({ results, loading }) {
  if (loading) return null;
  if (!results || results.length === 0) {
    return <p className="empty">No results yet. Try a query above.</p>;
  }
  return (
    <div>
      {results.map((r) => (
        <ResultCard key={r.docId} item={r} />
      ))}
    </div>
  );
}
