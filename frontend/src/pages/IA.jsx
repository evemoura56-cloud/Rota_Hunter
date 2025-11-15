import styles from "./IA.module.css";
import { IATable } from "../components/IATable";

export const IA = ({ registros, onTreinar }) => (
  <div className={styles.section}>
    <div className={styles.controls}>
      <button className={styles.primary} onClick={onTreinar}>
        Re-treinar modelo
      </button>
      <button>Exportar dataset</button>
    </div>
    <IATable registros={registros} />
  </div>
);
