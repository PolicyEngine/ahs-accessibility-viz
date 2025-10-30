import { useState } from 'react'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import ageData from '../data/accessibility_by_age.json'

const AccessibilityByAge = () => {
  const [selectedFeature, setSelectedFeature] = useState('No-step entrance')

  // Get unique features
  const features = [...new Set(ageData.map(d => d.feature))]

  // Filter data by selected feature
  const chartData = ageData
    .filter(d => d.feature === selectedFeature)
    .map(d => ({
      age: d.age_category,
      percent: Math.round(d.percent_with_feature * 10) / 10
    }))

  return (
    <div className="chart-container">
      <div className="controls">
        <label htmlFor="feature-select">Accessibility Feature:</label>
        <select
          id="feature-select"
          value={selectedFeature}
          onChange={(e) => setSelectedFeature(e.target.value)}
        >
          {features.map(feature => (
            <option key={feature} value={feature}>{feature}</option>
          ))}
        </select>
      </div>

      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={chartData} margin={{ top: 20, right: 30, left: 20, bottom: 60 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis
            dataKey="age"
            angle={-45}
            textAnchor="end"
            height={100}
          />
          <YAxis
            label={{ value: 'Percent of Units', angle: -90, position: 'insideLeft' }}
          />
          <Tooltip formatter={(value) => `${value}%`} />
          <Legend />
          <Bar dataKey="percent" name="% with Feature" fill="#2563eb" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

export default AccessibilityByAge
