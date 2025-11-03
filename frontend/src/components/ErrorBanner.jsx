export default function ErrorBanner({ message, onClose }) {
  if (!message) return null;
  return (
    <div className="error" role="alert">
      <span>{message}</span>
      <button onClick={onClose} aria-label="Dismiss error">
        ×
      </button>
    </div>
  );
}
