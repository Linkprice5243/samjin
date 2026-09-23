# 삼진어묵 명절 시즌 광고 성과 대시보드

추석(2026.08.01~09.21) vs 설날(2026.01.01~02.17) 통합 광고 성과를 GitHub Pages로 보는 정적 대시보드입니다.

## 파일 구성
- `index.html` — 대시보드 (성과 요약 / 매체별 비교 / 일자별 추이 / Meta 소재 성과 / 네이버 광고그룹)
- `data.js` — 보고서 데이터 (엑셀 `추석vs설날_데이터_분석_HookHold.xlsx` + Meta Ads MCP 조회값)
- `img/` — 소재 썸네일 (`{creative_id}.jpg`)
- `download_images.py` — 썸네일 일괄 다운로드 스크립트

## 올리는 순서
1. 이 폴더에서 `python download_images.py` 실행 → `img/`에 썸네일 34개 저장
   (Meta 이미지 링크는 임시 주소라 **9/27 전후 만료**되니 그 전에 실행)
2. 폴더 전체를 저장소에 푸시
3. Settings → Pages → Branch `main` / `(root)` 선택 후 저장

## 참고
- 영상 소재 썸네일은 API가 64px 크기만 줘서 흐릿할 수 있습니다. 선명하게 하려면 원본 썸네일을 같은 이름(`img/{creative_id}.jpg`)으로 덮어쓰면 됩니다.
- Hook Rate = 3초 영상재생 ÷ 노출, Hold Rate = ThruPlay(15초 이상 재생) ÷ 3초 영상재생 (영상 소재만).
  3초 재생은 광고 단위 원값이 API에 없어 `광고비 ÷ 3초 재생당 비용`으로 역산했습니다(±2% 내외).
