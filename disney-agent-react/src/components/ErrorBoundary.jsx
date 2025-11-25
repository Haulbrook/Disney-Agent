import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('ErrorBoundary caught an error:', error, errorInfo);
    this.setState({
      error,
      errorInfo
    });
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{
          padding: '40px',
          textAlign: 'center',
          fontFamily: 'Source Sans Pro, sans-serif'
        }}>
          <h1 style={{ color: '#746bab' }}>🏰 Oops! Something went wrong</h1>
          <p style={{ color: '#666', marginTop: '20px' }}>
            The Disney Trip Planner encountered an error. Please refresh the page to try again.
          </p>
          <button
            onClick={() => window.location.reload()}
            style={{
              marginTop: '20px',
              padding: '12px 30px',
              background: 'linear-gradient(135deg, #746bab 0%, #49FCD4 100%)',
              color: 'white',
              border: 'none',
              borderRadius: '50px',
              fontSize: '16px',
              cursor: 'pointer',
              fontWeight: '600'
            }}
          >
            Refresh Page
          </button>
          {process.env.NODE_ENV === 'development' && this.state.error && (
            <details style={{ marginTop: '40px', textAlign: 'left', maxWidth: '800px', margin: '40px auto' }}>
              <summary style={{ cursor: 'pointer', color: '#746bab', fontWeight: 'bold' }}>
                Error Details (Development Only)
              </summary>
              <pre style={{
                background: '#f5f5f5',
                padding: '20px',
                borderRadius: '10px',
                overflow: 'auto',
                fontSize: '14px',
                marginTop: '10px'
              }}>
                {this.state.error && this.state.error.toString()}
                {'\n\n'}
                {this.state.errorInfo && this.state.errorInfo.componentStack}
              </pre>
            </details>
          )}
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
