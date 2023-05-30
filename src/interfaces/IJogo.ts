import { ICampeonato } from "./ICampeonato";
import { ITime } from "./ITime";

export interface IJogo {
  id: number;
  data: Date;
  campeonato: ICampeonato;
  timeCasa: ITime;
  timeVisitante: ITime;
}
