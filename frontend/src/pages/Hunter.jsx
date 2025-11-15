import styles from "./Hunter.module.css";
import { HunterForm } from "../components/HunterForm";
import { CompanyList } from "../components/CompanyList";

export const Hunter = ({ empresas, onDiscover }) => (
  <div className={styles.wrapper}>
    <div>
      <h2>Motor Hunter Inteligente</h2>
      <HunterForm onDiscover={onDiscover} />
    </div>
    <div>
      <h2>Empresas encontradas</h2>
      <CompanyList empresas={empresas} />
    </div>
  </div>
);
