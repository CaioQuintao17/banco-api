const API = "http://127.0.0.1:8000"

// 🔹 mostra resultado na tela
function mostrarResultado(data) {
  document.getElementById("resultado").textContent =
    JSON.stringify(data, null, 2)
}

// 🔹 criar conta
async function criarConta() {

  const id = Number(
    document.getElementById("criarId").value
  )

  const saldo = Number(
    document.getElementById("saldoInicial").value
  )

  const response = await fetch(`${API}/conta`, {
    method: "POST",

    headers: {
      "Content-Type": "application/json"
    },

    body: JSON.stringify({
      id: id,
      saldo: saldo
    })
  })

  const data = await response.json()

  mostrarResultado(data)
}

// 🔹 consultar saldo
async function verSaldo() {

  const id = Number(
    document.getElementById("saldoId").value
  )

  const response = await fetch(`${API}/conta/${id}`)

  const data = await response.json()

  mostrarResultado(data)
}

// 🔹 depósito
async function depositar() {

  const id = Number(
    document.getElementById("depositoId").value
  )

  const valor = Number(
    document.getElementById("depositoValor").value
  )

  const response = await fetch(`${API}/conta/${id}/deposito`, {

    method: "POST",

    headers: {
      "Content-Type": "application/json"
    },

    body: JSON.stringify({
      valor: valor
    })
  })

  const data = await response.json()

  mostrarResultado(data)
}

// 🔹 saque
async function sacar() {

  const id = Number(
    document.getElementById("saqueId").value
  )

  const valor = Number(
    document.getElementById("saqueValor").value
  )

  const response = await fetch(`${API}/conta/${id}/saque`, {

    method: "POST",

    headers: {
      "Content-Type": "application/json"
    },

    body: JSON.stringify({
      valor: valor
    })
  })

  const data = await response.json()

  mostrarResultado(data)
}

// 🔹 transferência
async function transferir() {

  const origem = Number(
    document.getElementById("origemId").value
  )

  const destino = Number(
    document.getElementById("destinoId").value
  )

  const valor = Number(
    document.getElementById("transferenciaValor").value
  )

  const response = await fetch(
    `${API}/conta/${origem}/transferir`,
    {

      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
        conta_destino: destino,
        valor: valor
      })
    }
  )

  const data = await response.json()

  mostrarResultado(data)
}