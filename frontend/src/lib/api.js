const BASE_URL = import.meta.env.VITE_API_BASE || 'http://localhost:8000';

export async function generate(query) {
  const res = await fetch(`${BASE_URL}/generate`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query }),
  });
  if (!res.ok) {
    let msg = 'Unexpected error';
    try {
      const data = await res.json();
      if (data && data.detail) msg = data.detail;
      // eslint-disable-next-line no-empty
    } catch {}
    throw new Error(msg);
  }
  return res.json();
}
