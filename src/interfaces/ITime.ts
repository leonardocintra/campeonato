import { ICampeonato } from "./ICampeonato";

export interface ITime {
  id: number;
  nome: string;
  campeonatos: ICampeonato[];
}
