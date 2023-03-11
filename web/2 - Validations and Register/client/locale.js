export {
  tr,
  trDoc,
  setCurrentLanguage,
  UnknownMessageID,
  UnknownLanguage,
  onTournamentPage,
};

const userMessages = {
  en_US: {
    CHANGE_FORM: "Change form",
    WELCOME: "Welcome Administrator",
    IS_ADMIN:
      "If you're not an admin, leave this page please, I didn't have time to validate this.",
    INSERT_HERE: "Insert tournament",
    ERR_ENROLLING: "We were unable to proceed with the enrollment.",
    ERR_UNSPECIFIED_TOURNAMENT:
      "We're sorry but there was a problem with the enrolling data.",
    ERR_PLAYER_ALREADY_ENROLLED: "Player already enrolled at the tournament.",
    ERR_UNKNOWN_TOURNAMENT_ID:
      "We're sorry but there was a problem with the enrolling data.",
    ERR_TOURNAMENT_ALREADY_EXISTS: "Tournament already exists.",
    SUCCESS_ENROLLING: "successfully enrolled.",
    PLAYER: "Player",
    TOURNAMENT: "Tournament",
    EMAIL_ADDR: "Email address",
    TOURNAMENT_NAME_LABEL: "Tournament name *",
    TOURNAMENT_NAME: "Spring Tournament",
    TOURNAMENT_PRIZES: "Prizes up to 10th place",
    RULES: "Regulation",
    MEMBERS: "Members",
    ENROLL_HERE: "Register for tournament here",
    FULL_NAME_LABEL: "Full name",
    EMAIL_ADDR_LABEL: "Email",
    PHONE_NUMBER_LABEL: "Phone number",
    BIRTH_DATE_LABEL: "Birth date (DD/MM/YYYY)",
    PASSWORD_LABEL: "Password",
    REPEAT_PASSWORD_LABEL: "Password again",
    PLAYER_LEVEL_LABEL: "Level",
    START_DATE_LABEL: "Start date",
    END_DATE_LABEL: "End date",
    DATE_FMT: "(MM/DD/YYYY)",
    PRIVACY_POLICY_MSG: "I read and I agree with the ",
    PRIVACY_POLICY: "Privacy Policy",
    BEGINNER_LEVEL: "Beginner",
    INTERMEDIATE_LEVEL: "Intermediate",
    ADVANCED_LEVEL: "Advanced",
    PRE_PRO_LEVEL: "Pre-professional",
    PRO_LEVEL: "Professional",
    SELECT_TOURNAMENT_LABEL: "Tournament",
    SUBMIT_BTN: "Submit",
    RESET_BTN: "Reset",
  },
  pt_PT: {
    CHANGE_FORM: "Alterar formulário",
    WELCOME: "Bem-vindo Administrador",
    IS_ADMIN:
      "Se você não for um admin, saia desta página por favor, não tive tempo para validar isto.",
    INSERT_HERE: "Inserir torneio",
    ERR_ENROLLING: "Não foi possível concluir a inscrição.",
    ERR_UNSPECIFIED_TOURNAMENT:
      "Ooops...detectámos um problema com os dados de inscrição.",
    ERR_PLAYER_ALREADY_ENROLLED:
      "O jogador já se encontra inscrito no torneio.",
    ERR_UNKNOWN_TOURNAMENT_ID: "Ooops...torneio desconhecido.",
    ERR_TOURNAMENT_ALREADY_EXISTS: "Torneio já existe.",
    SUCCESS_ENROLLING: "inscrito com sucesso.",
    PLAYER: "Jogador",
    TOURNAMENT: "Torneio",
    EMAIL_ADDR: "Endereço de email",
    TOURNAMENT_NAME: "Torneio da Primavera",
    TOURNAMENT_NAME_LABEL: "Nome do torneio *",
    TOURNAMENT_PRIZES: "Prémios até ao 10º lugar",
    RULES: "Regulamento",
    MEMBERS: "Membros",
    ENROLL_HERE: "Inscreva-se aqui",
    FULL_NAME_LABEL: "Nome completo",
    EMAIL_ADDR_LABEL: "Email",
    PHONE_NUMBER_LABEL: "Telefone",
    BIRTH_DATE_LABEL: "Data de nascimento",
    PASSWORD_LABEL: "Senha",
    REPEAT_PASSWORD_LABEL: "Senha de novo",
    PLAYER_LEVEL_LABEL: "Nível",
    START_DATE_LABEL: "Data de início",
    END_DATE_LABEL: "Data de encerramento",
    DATE_FMT: "(DD/MM/AAAA)",
    PRIVACY_POLICY_MSG: "Li e concordo com a ",
    PRIVACY_POLICY: "Política de Privacidade",
    BEGINNER_LEVEL: "Iniciado",
    INTERMEDIATE_LEVEL: "Intermédio",
    ADVANCED_LEVEL: "Avançado",
    PRE_PRO_LEVEL: "Pré-profissional",
    PRO_LEVEL: "Profissional",
    SELECT_TOURNAMENT_LABEL: "Torneio",
    SUBMIT_BTN: "Submeter",
    RESET_BTN: "Limpar",
  },
};

class UnknownMessageID extends Error {}

class UnknownLanguage extends Error {}

let currentLanguage = "en_US";
let currentMessageId;
let currentResData;
let onTournamentPage = window.location.href.endsWith("-tournaments.html");

function translateMessage() {
  const msgDiv = document.querySelector(".submission-status");
  if (msgDiv.classList.length <= 1) {
    return;
  }
  msgDiv.innerHTML = tr(currentMessageId, currentResData, onTournamentPage);
}

function setCurrentLanguage({ target }) {
  const circleElement = target.closest("div");
  currentLanguage = currentLanguage === "en_US" ? "pt_PT" : "en_US";
  if (!userMessages[currentLanguage]) {
    throw new UnknownLanguage("Unknown language.");
  }
  circleElement.classList.toggle("in-action");
  trDoc(document.body);
  translateMessage();
}

function tr(messageID, responseData, isTournament) {
  if (!userMessages[currentLanguage][messageID]) {
    throw new UnknownMessageID("Unknown message id.");
  }
  [currentMessageId, currentResData] = [messageID, responseData];
  return createMessage(messageID, responseData, isTournament);
}

function createMessage(messageID, responseData, isTournament) {
  const isError = messageID.startsWith("ERR");
  const message = userMessages[currentLanguage][messageID];
  const messageCode = userMessages[currentLanguage][responseData];
  if (isError) {
    return `${message} ${messageCode}`;
  }

  if (isTournament) {
    const tourn = userMessages[currentLanguage]["TOURNAMENT"];
    return `${tourn} ${userMessages[currentLanguage][messageID]}<br>
    ${tourn}: ${responseData.name} <br>
    ID: ${responseData.id}`;
  }

  const player = userMessages[currentLanguage]["PLAYER"];
  return `${player} ${userMessages[currentLanguage][messageID]}<br>
  ${player}: ${responseData.full_name} <br>
  ID: ${responseData.id} <br>
  ${userMessages[currentLanguage]["EMAIL_ADDR"]}: ${responseData.email}`;
}

const trDoc = (function () {
  const trDocRe = /{{tr\s([A-Z_]+)\s?}}/;
  return function trDocs(ancestorNode) {
    const allElements = ancestorNode.querySelectorAll("*");
    let trcode;
    allElements.forEach((element) => {
      const codeFromDataAttr = element.dataset.trcode;
      if (codeFromDataAttr) {
        !element.placeholder
          ? (element.innerText =
              userMessages[currentLanguage][codeFromDataAttr])
          : (element.placeholder =
              userMessages[currentLanguage][codeFromDataAttr]);
        return;
      }
      if (
        ["DIV", "MAIN", "SPAN", "FORM", "SELECT", "I"].includes(
          element.nodeName
        )
      ) {
        return;
      }
      element.innerHTML = element.innerHTML.replace(trDocRe, (match, c1) => {
        trcode = c1;
        return userMessages[currentLanguage][c1];
      });
      element.placeholder &&= userMessages[currentLanguage][trcode];
      trcode && element.setAttribute("data-trcode", trcode);
    });
  };
})();
