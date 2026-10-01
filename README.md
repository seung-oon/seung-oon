<p><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img alt="Seungyoon Kim · Backend Developer · Medical AI Research" width="100%" src="assets/hero-light.svg">
</picture></p>

한성대학교 컴퓨터공학부 4학년<br>
추천 모델 **재현·평가 연구**와, 공간 DB·그래프 탐색 기반의 **백엔드**를 만듭니다.

✉&nbsp;[rlatmddbs02@gmail.com](mailto:rlatmddbs02@gmail.com) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/%EC%8A%B9%EC%9C%A4-%EA%B9%80-87099041a/) &nbsp;·&nbsp; [All repositories&nbsp;↗](https://github.com/seung-oon?tab=repositories)

<p>
<a href="#research"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stat-hidr-dark.svg">
  <img alt="HI-DR 재현 후 후보 풀 확장 재설계, Jaccard 0.4550에서 0.5231 (동일 추천 크기, 5-seed)" width="270" src="assets/stat-hidr-light.svg">
</picture></a>
<a href="#dcc-예선"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stat-dcc-dark.svg">
  <img alt="DCC 예선 신고자 성별 분류 정확도 0.9835 (Wav2Vec2, Validation 3,640통화)" width="270" src="assets/stat-dcc-light.svg">
</picture></a>
<a href="#projects"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stat-runify-dark.svg">
  <img alt="Runify 러닝 코스 생성 서버, Kafka와 pgRouting, 서버 전담 구현" width="270" src="assets/stat-runify-light.svg">
</picture></a>
</p>

[Research](#research) &nbsp;·&nbsp; [Projects](#projects) &nbsp;·&nbsp; [Tech&nbsp;Stack](#tech-stack) &nbsp;·&nbsp; [Others](#others)

## Research

### Drug Recommendation Research

MIMIC-III / IV 기반 의약품 추천 모델 재현성 연구 · 7개 트랙 · [repo&nbsp;↗](https://github.com/seung-oon/drug-recommendation-research)

<code>Python</code> <code>PyTorch</code> <code>MIMIC-III&nbsp;/&nbsp;IV</code>

> [!NOTE]
> 원본·행 단위 데이터는 포함하지 않고 코드·보고서·집계 결과만 공개합니다 (PhysioNet DUA 준수).

<table width="100%">
<tr>
<td width="140" align="center"><b>0.5231</b><br>Jaccard</td>
<td><sub>TRACK 02</sub><br><b>HI-DR (AAAI'25) 재현,<br>후보 풀 확장으로 재설계</b><br>기존 0.4550 → 0.5231<br>동일 추천 크기 · 5&#8209;seed</td>
</tr>
<tr>
<td width="140" align="center"><b>0.061</b><br>군집 간 격차</td>
<td><sub>TRACK 04</sub><br><b>SafeDrug 군집별 공정성 감사</b><br>보정 후 Jaccard 격차 · p&nbsp;0.003</td>
</tr>
<tr>
<td width="140" align="center"><b>절반</b><br>초과 DDI 격차</td>
<td><sub>TRACK 06</sub><br><b>SafeDrug DDI 제약 감사</b><br>페널티를 끄면 초과 DDI 격차가 절반으로 · 4&#8209;seed</td>
</tr>
</table>

<details>
<summary><b>트랙 01–07 전체 보기</b></summary>

<br>

| 트랙 | 요지 |
| --- | --- |
| **01** SOTA 논문 리뷰 | MR-DTR (WWW'25), CausalMed (CIKM'24), SubRec (NeurIPS'25) 정독, 데이터 자원·전처리 비교 |
| **02** HI-DR 재현 | "과다 추천을 걸러야 한다"는 1차 가설이 틀렸음을 확인하고, 사후 필터 대신 **이력 기반 후보 풀 확장**으로 재설계 (5-seed). 실제 운영 임계값 기준 Jaccard는 약 0.503 |
| **03** SafeDrug + 장기 기능 | ICD-9/10 통합 MIMIC-IV 레코드 재구축, 신·간 기능 지표 주입. 파이프라인 완성, GPU 스모크 테스트 단계 |
| **04** 군집별 공정성 감사 | 진단 텍스트로 방문을 군집화해 정확도 격차 검정. 재현 test Jaccard 0.508~0.515, precision 격차가 recall 격차의 2배. 개입 9종 시험 |
| **05** 급성 attention | 방문 표현을 입원 시점 텍스트 attention으로 교체. Jaccard 0.518까지 상승, 군집 격차는 그대로 |
| **06** DDI 제약 감사 | SafeDrug DDI 행렬이 TWOSIDES 비특이적 부작용 40종에 걸린 쌍이라 가이드라인 병용까지 상호작용으로 표시됨을 확인. 페널티를 끄면 초과 DDI 격차 절반 (4-seed) |
| **07** 급성/만성 사전검증 | 가설을 구현 전에 검증해 반증하고 방향 재설정. MIMIC-IV에서 kNN 검색 + 직전 처방 기준선(0.494)이 SafeDrug·GAMENet·MICRON(0.440~0.449)을 앞섬 |

</details>

### DCC 예선

119 신고 전화 음성·전사 데이터 AI 과제 · 팀 5인 · 2026.09 · [repo&nbsp;↗](https://github.com/KozzilzzilE/DCC_Problem)

<code>Python</code> <code>PyTorch</code> <code>Hugging&nbsp;Face&nbsp;Transformers</code> <code>scikit-learn</code> <code>pytest</code>

<table width="100%">
<tr>
<td width="140" align="center"><b>0.9835</b><br>정확도</td>
<td><sub>MISSION 1 · 단독 담당</sub><br><b>신고자 성별 분류</b><br>Wav2Vec2 · Validation 3,640통화</td>
</tr>
<tr>
<td width="140" align="center"><b>0.6546</b><br>Macro F1@0.5</td>
<td><sub>MISSION 3 · 제출 경로·학습 개선 담당</sub><br><b>환자 증상 다중 라벨 분류</b><br>기준선 0.5967<br>→ pos_weight 거듭제곱 0.6496<br>→ 앙상블 + 블렌드 0.6546</td>
</tr>
</table>

<details>
<summary><b>담당 내용 자세히</b></summary>

<br>

**Mission 1** — 조각 단위 학습 → 통화 단위 soft voting

- 통화 음성에서 신고자 발화만 잘라 **조각 단위 학습 → 통화 단위 soft voting** 구조 설계 (조각 정확도 0.88 → 통화 정확도 0.98)
- ResNet50(log-mel)·Wav2Vec2·전화 음성 사전학습 모델 3갈래 비교 하네스 구축, SpecAugment·지식 증류로 ResNet 개선
- 모델 간 오류 겹침 분석으로 앙상블 한계 확인
- 대회 규정(결정 임계값 0.5 고정)에 맞춰 제출 경로 정비, 오프라인 로딩·VRAM 페이징 등 1회 실행 채점 대비

**Mission 3** — 제출 추론 경로 구현, 임계값 대신 손실로 보정

- 더미 상태였던 **제출 추론 경로 구현** — 학습 설정을 체크포인트에서 복원해 학습-추론 불일치 차단, 임계값 0.5 고정을 코드로 강제
- 임계값 대신 손실로 보정 — 기존 pos_weight는 과보정으로 Macro F1 0.6189에 그쳐, `pos_weight` 거듭제곱 옵션을 추가해 과보정을 줄임
- KLUE-RoBERTa 멀티시드 앙상블 + **TF-IDF·LogisticRegression 블렌드**로 제출 번들 구성
- 발화 경계 전처리 모드, 적대적 리뷰 반영(자기완결 번들, 인코딩·BOM·NaN 처리), 규정 준수 pytest 회귀 테스트 추가

</details>

## Projects

### Runify · 러닝 코스 생성 서버

그린 도형을 실제 도보 도로망 위의 러닝 코스로 바꿔 주는 서비스<br>
**Backend · 코스 생성 서버 전담** · 팀 프로젝트 · 2026.08 · [repo&nbsp;↗](https://github.com/KozzilzzilE/Running-Sketch-Server)

- 도형 정규화 → 배치 탐색 → 도로 스냅 → `pgr_dijkstra` 스티칭 → 닮음도 채점·보정까지 **계산기하 + 그래프 탐색 파이프라인** 구현 (강남·서초 OSM 실그래프)
- 계단 경로가 곧은 경로보다 높게 채점되는 닮음도 결함을 **측정으로 확인**(0.9015 대 0.784)하고 채점 항을 추가해 해결. 효과가 없던 시도는 근거를 남기고 되돌림
- Kafka 요청 소비 → 결과 이벤트 발행. 수동 커밋·재시도 후 DLT, `generationId` 멱등, 정체 작업 자동 복구, Testcontainers 통합 테스트
- 코너가 많은 도형 등 알려진 한계는 이슈와 문서에 기록

<code>Java&nbsp;21</code> <code>Spring&nbsp;Boot&nbsp;4</code> <code>Kafka</code> <code>PostgreSQL&nbsp;+&nbsp;PostGIS&nbsp;+&nbsp;pgRouting</code> <code>Flyway</code> <code>Testcontainers</code> <code>Docker</code>

### Safe-walk · 지도 기반 안전 보행 서비스

**Team Lead · Backend** · 경기도 공공데이터 공모전 · 2026.07 · [repo&nbsp;↗](https://github.com/safe-waalk/BE)

- CCTV·보안등·안심벨·범죄주의구역·사용자 신고 데이터를 PostGIS에 적재, 좌표 반경 기반 **안전 인프라 집계·지도 레이어·안전점수 API** 제공
- ORM 없이 `NamedParameterJdbcTemplate`으로 공간 쿼리 직접 작성

<code>Java&nbsp;21</code> <code>Spring&nbsp;Boot&nbsp;4</code> <code>PostgreSQL&nbsp;+&nbsp;PostGIS&nbsp;(Supabase)</code> <code>Docker</code> <code>JUnit&nbsp;5</code>

### ShiftRhythm · 교대근무자 생체리듬 코칭 앱

**Backend** · 2026.08 · [repo&nbsp;↗](https://github.com/2026-1-midtone/Backend)

- 근무표 사진을 **Google Document AI OCR**로 인식해 일정 자동 입력 (서비스 계정 impersonation, 키 파일 없음)
- Testcontainers 기반 MySQL·Redis 통합 테스트, Docker Compose 로컬 환경

<code>Java&nbsp;21</code> <code>Spring&nbsp;Boot&nbsp;4</code> <code>MySQL</code> <code>Redis</code> <code>Docker</code> <code>Google&nbsp;Document&nbsp;AI</code>

### OnRoot AI · LLM 기반 자격증 학습 플래너

**Backend** · 2026.05 · [repo&nbsp;↗](https://github.com/On-root-AI/BE)

- Q-Net 공공데이터 API로 시험 일정을 받아 **Gemini API**로 맞춤 학습 계획 생성

<code>Java&nbsp;21</code> <code>Spring&nbsp;Boot&nbsp;3.5</code> <code>MySQL</code> <code>Spring&nbsp;Data&nbsp;JPA</code> <code>Gemini&nbsp;API</code>

## Tech Stack

<table width="100%">
<tr><td width="130"><b>Backend</b></td><td><code>Java</code> <code>Spring&nbsp;Boot</code> <code>MySQL</code> <code>PostgreSQL&nbsp;+&nbsp;PostGIS&nbsp;+&nbsp;pgRouting</code> <code>Redis</code> <code>Kafka</code></td></tr>
<tr><td width="130"><b>Infra</b></td><td><code>AWS</code> <code>GCP</code> <code>Docker</code> <code>GitHub&nbsp;Actions</code></td></tr>
<tr><td width="130"><b>AI / Research</b></td><td><code>Python</code> <code>PyTorch</code> <code>LangChain&nbsp;/&nbsp;RAG</code></td></tr>
</table>

## Others

- **[NextPerson](https://github.com/seung-oon/NextPerson)** — 은행 창구 업무 시뮬레이션 게임 (Unity 6). *Papers, Please* 구조에 금융 규제 판단을 적용
- **[멋쟁이사자처럼 14기 Backend 1팀](https://github.com/HSU-Likelion-Backend-14th/Team-1)** — Spring 기반 백엔드 과제 수행 · 2026.03–04

<br>

<sub>[↑ back to top](#top)</sub>

<p><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/footer-dark.svg">
  <img alt="" width="100%" src="assets/footer-light.svg">
</picture></p>
