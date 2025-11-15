import styles from "./Templates.module.css";
import { TemplateManager } from "../components/TemplateManager";

export const Templates = ({ templates, onSave }) => (
  <div className={styles.section}>
    <TemplateManager templates={templates} onSave={onSave} />
  </div>
);
