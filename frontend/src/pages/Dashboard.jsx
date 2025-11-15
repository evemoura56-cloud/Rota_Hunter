import styles from "./Dashboard.module.css";
import { KpiCard } from "../components/KpiCard";
import { ChartSection } from "../components/ChartSection";

export const Dashboard = ({ kpis, charts }) => (
  <div className={styles.wrapper}>
    <div className={styles.kpis}>
      {kpis.map((kpi) => (
        <KpiCard key={kpi.label} label={kpi.label} value={kpi.value} tag={kpi.tag} />
      ))}
    </div>
    <ChartSection pizza={charts.pizza} barras={charts.barras} linha={charts.linha} />
    <div className={styles.sectionBox}>
      <h3 style={{ marginTop: 0 }}>Velocidade do Funil</h3>
      <div className={styles.timeline}>
        {charts.velocidade.map((etapa) => (
          <div key={etapa.nome} className={styles.timelineItem}>
            <strong>{etapa.nome}</strong>
            <p style={{ margin: "6px 0 0", color: "var(--cinza-claro)" }}>{etapa.dias} dias</p>
          </div>
        ))}
      </div>
    </div>
  </div>
);
