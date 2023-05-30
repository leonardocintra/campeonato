import { IJogo } from "../interfaces/IJogo";
import { campeonato2023 } from "./campeonato";
import { timePraca, timeRanaModas } from "./time";

const jogo1: IJogo = {
  id: 1,
  campeonato: campeonato2023,
  data: new Date("2023-06-01"),
  timeCasa: timePraca,
  timeVisitante: timeRanaModas,
};
