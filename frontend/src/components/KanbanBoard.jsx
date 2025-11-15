import { DragDropContext, Droppable, Draggable } from "@hello-pangea/dnd";
import styles from "./KanbanBoard.module.css";

const statusOrder = ["PROSPECTADO", "CONTATADO", "RESPONDEU", "QUALIFICADO", "PROPOSTA", "GANHO", "PERDIDO"];

export const KanbanBoard = ({ colunas, onMove }) => {
  const handleDragEnd = ({ source, destination }) => {
    if (!destination) return;
    onMove(source, destination);
  };

  return (
    <DragDropContext onDragEnd={handleDragEnd}>
      <div className={styles.board}>
        {statusOrder.map((status) => (
          <Droppable droppableId={status} key={status}>
            {(provided) => (
              <div ref={provided.innerRef} {...provided.droppableProps} className={styles.column}>
                <h4>{status}</h4>
                {colunas[status].map((lead, index) => (
                  <Draggable draggableId={lead.id.toString()} index={index} key={lead.id}>
                    {(dragProvided) => (
                      <div ref={dragProvided.innerRef} {...dragProvided.draggableProps} {...dragProvided.dragHandleProps} className={styles.card}>
                        <strong>{lead.nome}</strong>
                        <span>{lead.setor}</span>
                        <span>p_win {lead.pwin}%</span>
                      </div>
                    )}
                  </Draggable>
                ))}
                {provided.placeholder}
              </div>
            )}
          </Droppable>
        ))}
      </div>
    </DragDropContext>
  );
};
