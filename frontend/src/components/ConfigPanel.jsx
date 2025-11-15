import styles from "./ConfigPanel.module.css";

export const ConfigPanel = ({ dados }) => (
  <div className={styles.panel}>
    {dados.map((item) => (
      <div key={item.label} className={styles.row}>
        <span>{item.label}</span>
        <strong>{item.valor}</strong>
      </div>
    ))}
  </div>
);
