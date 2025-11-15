import styles from "./KpiCard.module.css";

export const KpiCard = ({ label, value, tag }) => (
  <div className={styles.card}>
    <span className={styles.label}>{label}</span>
    <span className={styles.value}>{value}</span>
    {tag && <span className={styles.tag}>{tag}</span>}
  </div>
);
