import { useState } from 'react'
import AccessibilityByAge from './components/AccessibilityByAge'
import AccessibilityByStructure from './components/AccessibilityByStructure'

function App() {
  return (
    <div className="App">
      <header>
        <h1>Housing Accessibility Features in America</h1>
        <p className="description">
          Analysis of accessibility features in the U.S. housing stock using the 2019 American Housing Survey.
          Based on weighted estimates from 63,000+ housing units representing 127 million occupied units nationwide.
        </p>
        <p className="description" style={{ fontStyle: 'italic', fontSize: '0.95em' }}>
          This visualization extends HUD's 2011 accessibility study using real AHS 2019 microdata.
        </p>
      </header>

      <section>
        <h2>Accessibility by Building Age</h2>
        <p className="description">
          Newer buildings are more likely to include accessibility features due to evolving building codes and design standards.
        </p>
        <AccessibilityByAge />
      </section>

      <section>
        <h2>Accessibility by Structure Type</h2>
        <p className="description">
          Accessibility patterns vary by building type and feature. Large multifamily buildings often provide
          single-floor living (bedroom and bathroom on entry level) due to elevators and single-level unit designs.
          Single-family homes more commonly have wheelchair ramps, reflecting individual modifications.
        </p>
        <p className="description" style={{ fontSize: '0.9em', fontStyle: 'italic', background: '#fff9e6', padding: '0.5em', borderRadius: '4px' }}>
          Note: This analyzes all housing units. HUD's 2019 report focused specifically on households with accessibility needs,
          finding 73% of large apartments (10+ units) with accessibility needs had single-floor living vs. 61% of single-family homes.
        </p>
        <AccessibilityByStructure />
      </section>

      <footer style={{ marginTop: '4em', paddingTop: '2em', borderTop: '1px solid #ccc', fontSize: '0.9em', color: '#666' }}>
        <p>
          Data source: American Housing Survey 2019 (accessibility module).
          Analysis by PolicyEngine.
          <br />
          Original HUD study: <a href="https://www.huduser.gov/portal/sites/default/files/pdf/accessibility-america-housingStock.pdf" target="_blank" rel="noopener noreferrer">
            Accessibility of America's Housing Stock (2011)
          </a>
        </p>
      </footer>
    </div>
  )
}

export default App
