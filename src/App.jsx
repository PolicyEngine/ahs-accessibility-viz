import { useState } from 'react'
import AccessibilityByAge from './components/AccessibilityByAge'
import AccessibilityByStructure from './components/AccessibilityByStructure'

function App() {
  return (
    <div className="App">
      <header>
        <h1>Housing Accessibility Features in America</h1>
        <p className="description">
          Analysis of accessibility features in the U.S. housing stock using the American Housing Survey.
          This visualization replicates and extends HUD's 2011 study using 2019 data.
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
          Large multifamily buildings typically have more accessibility features than smaller structures,
          partly due to Fair Housing Act requirements for buildings with 4+ units built after 1991.
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
