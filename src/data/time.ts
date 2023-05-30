import { ITime } from "../interfaces/ITime";
import { campeonato2023 } from "./campeonato";

const timePraca: ITime = {
  id: 1,
  nome: "Praça FC",
  campeonatos: [campeonato2023],
};

const timeRanaModas: ITime = {
  id: 2,
  nome: "Rana Modas",
  campeonatos: [campeonato2023],
};

export { timePraca, timeRanaModas };
