export default function SearchBar({ query, setQuery, onSubmit, loading }) {
  return (
    <form onSubmit={onSubmit} className="searchBar">
      <label htmlFor="q" className="visually-hidden">
        Query
      </label>
      <input
        id="q"
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="e.g., price fixing, termination clause"
        aria-label="Search query"
      />
      <button type="submit" disabled={loading} aria-busy={loading}>
        {loading ? 'Searching…' : 'Summarize'}
      </button>
    </form>
  );
}
