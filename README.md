# analise_instagram

Um script Python simples, leve e seguro para analisar quem não te segue de volta no Instagram, além de identificar quem você não está seguindo de volta.

Ao contrário de aplicativos de terceiros que exigem o login da sua conta (e que frequentemente causam o banimento do perfil), este script funciona de forma **100% offline e segura**, processando diretamente os dados que o próprio Instagram fornece na Central de Contas.

---

## 🚀 Como Funciona

O script utiliza **Teoria dos Conjuntos** (através de estruturas `set()` do Python) para mapear e cruzar os dados extraídos dos arquivos JSON do seu histórico do Instagram:

* **Quem não retornou o follow:** Calculado através da diferença de conjuntos: $\text{Seguidos} - \text{Seguidores}$.
* **Quem você não retornou o follow:** Calculado através da diferença de conjuntos: $\text{Seguidores} - \text{Seguidos}$.

---

## 🛠️ Passo a Passo: Como Usar

### 1. Baixar seus dados do Instagram
1. Acesse o Instagram (de preferência pelo computador) e vá em **Configurações**.
2. Acesse a **Central de Contas** > **Suas informações e permissões** > **Baixar suas informações**.
3. Escolha **Baixar ou transferir informação** e selecione o seu perfil.
4. Escolha **Tipos específicos de informação** e marque apenas **Seguidores e seguindo** (isso faz o arquivo ser gerado muito mais rápido).
5. **MUITO IMPORTANTE:** Na tela de configurações do arquivo, mude o formato de HTML para **JSON**.
6. Clique em **Solicitar download** e aguarde o e-mail de confirmação do Instagram para baixar o arquivo `.zip`.

### 2. Preparar o Ambiente
1. Extraia o arquivo `.zip` baixado do Instagram.
2. Navegue pelas pastas extraídas até encontrar o diretório: `connections/followers_and_following/`.
3. Copie os arquivos `followers_1.json` e `following.json` para dentro da **mesma pasta** onde está o script deste repositório.

### 3. Executar o Script
Com os arquivos JSON na mesma pasta do script, abra o seu terminal e execute:

```bash
python analisar_instagram.py
