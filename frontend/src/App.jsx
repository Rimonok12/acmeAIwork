import { useRef, useState } from 'react';
import { generate } from './lib/api';
import './App.css';
export default function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const resultsRef = useRef(null);

  const onSubmit = async (e) => {
    e.preventDefault();
    const q = query.trim();
    if (!q) {
      setError('Please type a query.');
      return;
    }
    setError('');
    setLoading(true);
    setResults([]);
    try {
      const data = await generate(q);
      setResults(data.results || []);
      setTimeout(() => {
        resultsRef.current?.scrollIntoView({ behavior: 'smooth' });
      }, 0);
    } catch (err) {
      setError(err.message || 'Server error.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-linear-to-br from-gray-50 to-gray-100 py-10">
      <main className="max-w-3xl mx-auto px-5">
        <div className="bg-white shadow-lg rounded-2xl p-6">
          <h1 className="text-3xl font-semibold text-blue-700 mb-6 text-center">
            Legal Document Search (Bangladesh • Mock)
          </h1>

          {error && (
            <div className="bg-red-100 text-red-700 px-4 py-2 rounded-lg mb-4 flex justify-between items-center">
              <span>{error}</span>
              <button
                onClick={() => setError('')}
                className="font-bold text-lg leading-none hover:text-red-900"
                aria-label="Dismiss error"
              >
                ×
              </button>
            </div>
          )}

          <form onSubmit={onSubmit} className="flex gap-3 mb-6">
            <label htmlFor="q" className="sr-only">
              Query
            </label>
            <input
              id="q"
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="e.g., price fixing, bid rigging, termination"
              className="flex-1 border border-gray-300 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500 transition"
            />
            <button
              type="submit"
              disabled={loading}
              className={`rounded-xl px-5 py-3 text-white font-medium ${
                loading
                  ? 'bg-blue-300 cursor-not-allowed'
                  : 'bg-blue-600 hover:bg-blue-700'
              } transition`}
            >
              {loading ? 'Searching…' : 'Search'}
            </button>
          </form>

          {loading && (
            <div className="text-center text-gray-500 mb-6 animate-pulse">
              Searching…
            </div>
          )}

          <section ref={resultsRef}>
            {!loading && results.length === 0 && (
              <p className="text-center text-gray-400 italic">
                No results yet. Try a query above.
              </p>
            )}

            {results.map((r) => {
              const matchedClasses = r.matched
                ? 'bg-green-50 ring-1 ring-green-200'
                : 'bg-white';

              return (
                <article
                  key={r.docId}
                  className={`border border-gray-200 rounded-2xl mb-5 p-5 transition hover:shadow-md ${matchedClasses}`}
                >
                  <div className="flex justify-between items-start mb-2">
                    <h2 className="text-xl font-semibold text-gray-800">
                      {r.title}
                    </h2>
                    {r.matched && (
                      <span className="text-xs bg-green-200 text-green-900 px-2 py-1 rounded-full font-medium">
                        Match
                      </span>
                    )}
                  </div>
                  <p className="text-gray-700 leading-relaxed">{r.summary}</p>
                </article>
              );
            })}
          </section>
        </div>
      </main>
    </div>
  );
}
