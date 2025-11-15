import styles from "./Configuracoes.module.css";
import { ConfigPanel } from "../components/ConfigPanel";

export const Configuracoes = ({ dados }) => (
  <div className={styles.section}>
    <ConfigPanel dados={dados} />
  </div>
);
