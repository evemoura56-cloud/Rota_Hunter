import { PieChart, Pie, Cell, BarChart, Bar, XAxis, YAxis, Tooltip, LineChart, Line, ResponsiveContainer } from "recharts";
import styles from "./ChartSection.module.css";

const palette = ["#ff2e4c", "#b3122c", "#e6e6e6", "#ff6273", "#ff94a3"];

export const ChartSection = ({ pizza, barras, linha }) => (
  <div className={styles.section}>
    <div className={styles.panel}>
      <h4>Distribuição por Setor</h4>
      <ResponsiveContainer width="100%" height={220}>
        <PieChart>
          <Pie data={pizza} dataKey="valor" nameKey="nome" innerRadius={55} outerRadius={80} stroke="none">
            {pizza.map((_, index) => (
              <Cell key={index} fill={palette[index % palette.length]} />
            ))}
          </Pie>
          <Tooltip contentStyle={{ background: "#111", border: "none" }} />
        </PieChart>
      </ResponsiveContainer>
    </div>
    <div className={styles.panel}>
      <h4>Leads por Status</h4>
      <ResponsiveContainer width="100%" height={220}>
        <BarChart data={barras}>
          <XAxis dataKey="nome" stroke="#999" />
          <YAxis stroke="#666" />
          <Tooltip contentStyle={{ background: "#111", border: "none" }} />
          <Bar dataKey="valor" radius={[6, 6, 0, 0]} fill="url(#gradBar)">
            <defs>
              <linearGradient id="gradBar" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stopColor="#ff2e4c" />
                <stop offset="100%" stopColor="#b3122c" />
              </linearGradient>
            </defs>
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
    <div className={styles.panel}>
      <h4>Evolução Semanal</h4>
      <ResponsiveContainer width="100%" height={220}>
        <LineChart data={linha}>
          <XAxis dataKey="dia" stroke="#999" />
          <YAxis stroke="#666" />
          <Tooltip contentStyle={{ background: "#111", border: "none" }} />
          <Line type="monotone" dataKey="valor" stroke="#ff2e4c" strokeWidth={3} dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  </div>
);
