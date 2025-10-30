import { useState } from 'react'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import structureData from '../data/accessibility_by_structure.json'

const AccessibilityByStructure = () => {
  const [selectedFeature, setSelectedFeature] = useState('No-step entrance')

  // Get unique features
  const features = [...new Set(structureData.map(d => d.feature))]

  // Define structure type order
  const structureOrder = {
    'Single-family detached': 0,
    'Single-family attached': 1,
    'Mobile home/other': 2,
    '2-4 units': 3,
    '5-49 units': 4,
    '50+ units': 5
  }

  // Filter data by selected feature and sort by structure type
  const chartData = structureData
    .filter(d => d.feature === selectedFeature)
    .map(d => ({
      structure: d.structure_type,
      percent: Math.round(d.percent_with_feature * 10) / 10
    }))
    .sort((a, b) => structureOrder[a.structure] - structureOrder[b.structure])

  return (
    <div className="chart-container">
      <div className="controls">
        <label htmlFor="structure-feature-select">Accessibility Feature:</label>
        <select
          id="structure-feature-select"
          value={selectedFeature}
          onChange={(e) => setSelectedFeature(e.target.value)}
        >
          {features.map(feature => (
            <option key={feature} value={feature}>{feature}</option>
          ))}
        </select>
      </div>

      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={chartData} margin={{ top: 20, right: 30, left: 20, bottom: 80 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis
            dataKey="structure"
            angle={-45}
            textAnchor="end"
            height={120}
          />
          <YAxis
            label={{ value: 'Percent of Units', angle: -90, position: 'insideLeft' }}
          />
          <Tooltip formatter={(value) => `${value}%`} />
          <Legend />
          <Bar dataKey="percent" name="% with Feature" fill="#16a34a" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

export default AccessibilityByStructure
