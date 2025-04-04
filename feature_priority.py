import pandas as pd

# 1. 사용자 관리
user_management = [
    # 1.1 사용자 기본 관리
    {"모듈": "사용자 관리", "하위 모듈": "사용자 기본 관리", "기능ID": "UM-101", "기능명": "createUser", "설명": "신규 사용자 생성", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 기본 관리", "기능ID": "UM-102", "기능명": "getUserById", "설명": "사용자 ID로 사용자 정보 조회", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 기본 관리", "기능ID": "UM-103", "기능명": "getUserList", "설명": "사용자 목록 조회 (필터링/페이징 지원)", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 기본 관리", "기능ID": "UM-104", "기능명": "updateUser", "설명": "사용자 정보 업데이트", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 기본 관리", "기능ID": "UM-105", "기능명": "deleteUser", "설명": "사용자 삭제", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 기본 관리", "기능ID": "UM-106", "기능명": "enableUser", "설명": "사용자 활성화", "우선순위": "중"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 기본 관리", "기능ID": "UM-107", "기능명": "disableUser", "설명": "사용자 비활성화", "우선순위": "중"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 기본 관리", "기능ID": "UM-108", "기능명": "resetUserPassword", "설명": "사용자 비밀번호 초기화", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 기본 관리", "기능ID": "UM-109", "기능명": "exportUserList", "설명": "사용자 목록 내보내기", "우선순위": "중"},

    # 1.2 사용자 그룹 관리
    {"모듈": "사용자 관리", "하위 모듈": "사용자 그룹 관리", "기능ID": "UG-101", "기능명": "createUserGroup", "설명": "사용자 그룹 생성", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 그룹 관리", "기능ID": "UG-102", "기능명": "getUserGroupList", "설명": "사용자 그룹 목록 조회", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 그룹 관리", "기능ID": "UG-103", "기능명": "updateUserGroup", "설명": "사용자 그룹 정보 업데이트", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 그룹 관리", "기능ID": "UG-104", "기능명": "deleteUserGroup", "설명": "사용자 그룹 삭제", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 그룹 관리", "기능ID": "UG-105", "기능명": "enableUserGroup", "설명": "사용자 그룹 활성화", "우선순위": "중"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 그룹 관리", "기능ID": "UG-106", "기능명": "disableUserGroup", "설명": "사용자 그룹 비활성화", "우선순위": "중"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 그룹 관리", "기능ID": "UG-107", "기능명": "addUserToGroup", "설명": "그룹에 사용자 추가", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 그룹 관리", "기능ID": "UG-108", "기능명": "removeUserFromGroup", "설명": "그룹에서 사용자 제거", "우선순위": "상"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 그룹 관리", "기능ID": "UG-109", "기능명": "getUsersInGroup", "설명": "그룹 내 사용자 목록 조회", "우선순위": "상"},

    # 1.3 사용자 활동 관리
    {"모듈": "사용자 관리", "하위 모듈": "사용자 활동 관리", "기능ID": "UA-101", "기능명": "getUserActivity", "설명": "사용자 활동 로그 조회", "우선순위": "중"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 활동 관리", "기능ID": "UA-102", "기능명": "getUserUsage", "설명": "사용자 리소스 사용량 조회", "우선순위": "중"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 활동 관리", "기능ID": "UA-103", "기능명": "getUserApiCalls", "설명": "사용자 API 호출 내역 조회", "우선순위": "중"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 활동 관리", "기능ID": "UA-104", "기능명": "getUserSessionData", "설명": "사용자 세션 데이터 조회", "우선순위": "중"},
    {"모듈": "사용자 관리", "하위 모듈": "사용자 활동 관리", "기능ID": "UA-105", "기능명": "getUserDeployedServices", "설명": "사용자 배포 서비스 목록 조회", "우선순위": "중"}
]

# 2. 권한 관리
permission_management = [
    # 2.1 권한 그룹 관리
    {"모듈": "권한 관리", "하위 모듈": "권한 그룹 관리", "기능ID": "PG-101", "기능명": "createPermissionGroup", "설명": "권한 그룹 생성", "우선순위": "상"},
    {"모듈": "권한 관리", "하위 모듈": "권한 그룹 관리", "기능ID": "PG-102", "기능명": "getPermissionGroupList", "설명": "권한 그룹 목록 조회", "우선순위": "상"},
    {"모듈": "권한 관리", "하위 모듈": "권한 그룹 관리", "기능ID": "PG-103", "기능명": "updatePermissionGroup", "설명": "권한 그룹 업데이트", "우선순위": "상"},
    {"모듈": "권한 관리", "하위 모듈": "권한 그룹 관리", "기능ID": "PG-104", "기능명": "deletePermissionGroup", "설명": "권한 그룹 삭제", "우선순위": "상"},
    {"모듈": "권한 관리", "하위 모듈": "권한 그룹 관리", "기능ID": "PG-105", "기능명": "getPermissionGroupDetail", "설명": "권한 그룹 상세 정보 조회", "우선순위": "상"},
    {"모듈": "권한 관리", "하위 모듈": "권한 그룹 관리", "기능ID": "PG-106", "기능명": "duplicatePermissionGroup", "설명": "권한 그룹 복제", "우선순위": "중"},

    # 2.2 권한 설정 관리
    {"모듈": "권한 관리", "하위 모듈": "권한 설정 관리", "기능ID": "PS-101", "기능명": "assignPermissionToGroup", "설명": "그룹에 권한 할당", "우선순위": "상"},
    {"모듈": "권한 관리", "하위 모듈": "권한 설정 관리", "기능ID": "PS-102", "기능명": "removePermissionFromGroup", "설명": "그룹에서 권한 제거", "우선순위": "상"},
    {"모듈": "권한 관리", "하위 모듈": "권한 설정 관리", "기능ID": "PS-103", "기능명": "assignUserToPermissionGroup", "설명": "사용자에게 권한 그룹 할당", "우선순위": "상"},
    {"모듈": "권한 관리", "하위 모듈": "권한 설정 관리", "기능ID": "PS-104", "기능명": "removeUserFromPermissionGroup", "설명": "사용자에서 권한 그룹 제거", "우선순위": "상"},
    {"모듈": "권한 관리", "하위 모듈": "권한 설정 관리", "기능ID": "PS-105", "기능명": "getUserPermissions", "설명": "사용자 권한 목록 조회", "우선순위": "상"},
    {"모듈": "권한 관리", "하위 모듈": "권한 설정 관리", "기능ID": "PS-106", "기능명": "checkUserPermission", "설명": "사용자 특정 권한 확인", "우선순위": "상"},

    # 2.3 권한 정책 관리
    {"모듈": "권한 관리", "하위 모듈": "권한 정책 관리", "기능ID": "PP-101", "기능명": "createPermissionPolicy", "설명": "권한 정책 생성", "우선순위": "중"},
    {"모듈": "권한 관리", "하위 모듈": "권한 정책 관리", "기능ID": "PP-102", "기능명": "updatePermissionPolicy", "설명": "권한 정책 업데이트", "우선순위": "중"},
    {"모듈": "권한 관리", "하위 모듈": "권한 정책 관리", "기능ID": "PP-103", "기능명": "getPermissionPolicyList", "설명": "권한 정책 목록 조회", "우선순위": "중"},
    {"모듈": "권한 관리", "하위 모듈": "권한 정책 관리", "기능ID": "PP-104", "기능명": "deletePermissionPolicy", "설명": "권한 정책 삭제", "우선순위": "중"},
    {"모듈": "권한 관리", "하위 모듈": "권한 정책 관리", "기능ID": "PP-105", "기능명": "applyPermissionPolicy", "설명": "권한 정책 적용", "우선순위": "중"}
]

# 3. 메뉴 관리
menu_management = [
    # 5.1 메뉴 구조 관리
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 구조 관리", "기능ID": "MS-101", "기능명": "createMenuStructure", "설명": "메뉴 구조 생성", "우선순위": "중"},
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 구조 관리", "기능ID": "MS-102", "기능명": "getMenuStructure", "설명": "메뉴 구조 조회", "우선순위": "중"},
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 구조 관리", "기능ID": "MS-103", "기능명": "updateMenuStructure", "설명": "메뉴 구조 업데이트", "우선순위": "중"},
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 구조 관리", "기능ID": "MS-104", "기능명": "deleteMenuStructure", "설명": "메뉴 구조 삭제", "우선순위": "중"},

    # 5.2 메뉴 접근 권한 관리
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 접근 권한 관리", "기능ID": "MP-101", "기능명": "setMenuPermission", "설명": "메뉴 접근 권한 설정", "우선순위": "중"},
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 접근 권한 관리", "기능ID": "MP-102", "기능명": "getMenuPermissionList", "설명": "메뉴 접근 권한 목록 조회", "우선순위": "중"},
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 접근 권한 관리", "기능ID": "MP-103", "기능명": "updateMenuPermission", "설명": "메뉴 접근 권한 업데이트", "우선순위": "중"},
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 접근 권한 관리", "기능ID": "MP-104", "기능명": "removeMenuPermission", "설명": "메뉴 접근 권한 제거", "우선순위": "중"},

    # 5.3 메뉴 커스터마이징
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 커스터마이징", "기능ID": "MC-101", "기능명": "createCustomMenu", "설명": "사용자 정의 메뉴 생성", "우선순위": "하"},
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 커스터마이징", "기능ID": "MC-102", "기능명": "updateCustomMenu", "설명": "사용자 정의 메뉴 업데이트", "우선순위": "하"},
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 커스터마이징", "기능ID": "MC-103", "기능명": "deleteCustomMenu", "설명": "사용자 정의 메뉴 삭제", "우선순위": "하"},
    {"모듈": "메뉴 관리", "하위 모듈": "메뉴 커스터마이징", "기능ID": "MC-104", "기능명": "setMenuLocalization", "설명": "메뉴 다국어 설정", "우선순위": "하"}
]

# 4. LLM 모델 관리
llm_management = [
    # 6.1 LLM 모델 기본 관리
    {"모듈": "LLM 모델 관리", "하위 모듈": "LLM 모델 기본 관리", "기능ID": "LM-101", "기능명": "registerLLMModel", "설명": "LLM 모델 등록", "우선순위": "상"},
    {"모듈": "LLM 모델 관리", "하위 모듈": "LLM 모델 기본 관리", "기능ID": "LM-102", "기능명": "getLLMModelList", "설명": "LLM 모델 목록 조회", "우선순위": "상"},
    {"모듈": "LLM 모델 관리", "하위 모듈": "LLM 모델 기본 관리", "기능ID": "LM-103", "기능명": "updateLLMModel", "설명": "LLM 모델 정보 업데이트", "우선순위": "상"},
    {"모듈": "LLM 모델 관리", "하위 모듈": "LLM 모델 기본 관리", "기능ID": "LM-104", "기능명": "deleteLLMModel", "설명": "LLM 모델 삭제", "우선순위": "상"},
    {"모듈": "LLM 모델 관리", "하위 모듈": "LLM 모델 기본 관리", "기능ID": "LM-105", "기능명": "activateLLMModel", "설명": "LLM 모델 활성화", "우선순위": "상"},
    {"모듈": "LLM 모델 관리", "하위 모듈": "LLM 모델 기본 관리", "기능ID": "LM-106", "기능명": "deactivateLLMModel", "설명": "LLM 모델 비활성화", "우선순위": "상"},

    # 6.2 LLM 모델 사용량 분석
    {"모듈": "LLM 모델 관리", "하위 모듈": "LLM 모델 사용량 분석", "기능ID": "LA-101", "기능명": "getModelTokenUsage", "설명": "모델 토큰 사용량 조회", "우선순위": "상"},
    {"모듈": "LLM 모델 관리", "하위 모듈": "LLM 모델 사용량 분석", "기능ID": "LA-102", "기능명": "getModelUsageByUser", "설명": "사용자별 모델 사용량 조회", "우선순위": "상"},
    {"모듈": "LLM 모델 관리", "하위 모듈": "LLM 모델 사용량 분석", "기능ID": "LA-103", "기능명": "getModelUsageByProject", "설명": "프로젝트별 모델 사용량 조회", "우선순위": "상"},
    {"모듈": "LLM 모델 관리", "하위 모듈": "LLM 모델 사용량 분석", "기능ID": "LA-104", "기능명": "exportModelUsageReport", "설명": "모델 사용량 보고서 내보내기", "우선순위": "중"}
]

# 5. 배포 서비스 관리
deployment_management = [
    # 7.1 연동 엔드포인트 관리
    {"모듈": "배포 서비스 관리", "하위 모듈": "연동 엔드포인트 관리", "기능ID": "EM-101", "기능명": "createApiEndpoint", "설명": "API 엔드포인트 생성", "우선순위": "상"},
    {"모듈": "배포 서비스 관리", "하위 모듈": "연동 엔드포인트 관리", "기능ID": "EM-102", "기능명": "getApiEndpointList", "설명": "API 엔드포인트 목록 조회", "우선순위": "상"},
    {"모듈": "배포 서비스 관리", "하위 모듈": "연동 엔드포인트 관리", "기능ID": "EM-103", "기능명": "updateApiEndpoint", "설명": "API 엔드포인트 업데이트", "우선순위": "상"},
    {"모듈": "배포 서비스 관리", "하위 모듈": "연동 엔드포인트 관리", "기능ID": "EM-104", "기능명": "deleteApiEndpoint", "설명": "API 엔드포인트 삭제", "우선순위": "상"},
    {"모듈": "배포 서비스 관리", "하위 모듈": "연동 엔드포인트 관리", "기능ID": "EM-105", "기능명": "setEndpointSecurity", "설명": "엔드포인트 보안 설정", "우선순위": "상"},

    # 7.2 어시스턴트 관리
    {"모듈": "배포 서비스 관리", "하위 모듈": "어시스턴트 관리", "기능ID": "AM-101", "기능명": "getAssistantList", "설명": "어시스턴트 목록 조회", "우선순위": "상"},
    {"모듈": "배포 서비스 관리", "하위 모듈": "어시스턴트 관리", "기능ID": "AM-102", "기능명": "getAssistantDetail", "설명": "어시스턴트 상세 정보 조회", "우선순위": "상"},
    {"모듈": "배포 서비스 관리", "하위 모듈": "어시스턴트 관리", "기능ID": "AM-103", "기능명": "deleteAssistant", "설명": "어시스턴트 삭제", "우선순위": "상"},
    {"모듈": "배포 서비스 관리", "하위 모듈": "어시스턴트 관리", "기능ID": "AM-104", "기능명": "getAssistantDeletionLog", "설명": "어시스턴트 삭제 로그 조회", "우선순위": "중"}
]

# 6. 용어사전 관리
dictionary_management = [
    # 8.1 용어사전 기본 관리
    {"모듈": "용어사전 관리", "하위 모듈": "용어사전 기본 관리", "기능ID": "DM-101", "기능명": "createDictionary", "설명": "용어사전 생성", "우선순위": "중"},
    {"모듈": "용어사전 관리", "하위 모듈": "용어사전 기본 관리", "기능ID": "DM-102", "기능명": "getDictionaryList", "설명": "용어사전 목록 조회", "우선순위": "중"},
    {"모듈": "용어사전 관리", "하위 모듈": "용어사전 기본 관리", "기능ID": "DM-103", "기능명": "updateDictionary", "설명": "용어사전 업데이트", "우선순위": "중"},
    {"모듈": "용어사전 관리", "하위 모듈": "용어사전 기본 관리", "기능ID": "DM-104", "기능명": "deleteDictionary", "설명": "용어사전 삭제", "우선순위": "중"},
    {"모듈": "용어사전 관리", "하위 모듈": "용어사전 기본 관리", "기능ID": "DM-105", "기능명": "activateDictionary", "설명": "용어사전 활성화", "우선순위": "중"},
    {"모듈": "용어사전 관리", "하위 모듈": "용어사전 기본 관리", "기능ID": "DM-106", "기능명": "deactivateDictionary", "설명": "용어사전 비활성화", "우선순위": "중"},

    # 8.2 용어 관리
    {"모듈": "용어사전 관리", "하위 모듈": "용어 관리", "기능ID": "TM-101", "기능명": "addTerm", "설명": "용어 추가", "우선순위": "중"},
    {"모듈": "용어사전 관리", "하위 모듈": "용어 관리", "기능ID": "TM-102", "기능명": "getTermList", "설명": "용어 목록 조회", "우선순위": "중"},
    {"모듈": "용어사전 관리", "하위 모듈": "용어 관리", "기능ID": "TM-103", "기능명": "updateTerm", "설명": "용어 업데이트", "우선순위": "중"},
    {"모듈": "용어사전 관리", "하위 모듈": "용어 관리", "기능ID": "TM-104", "기능명": "deleteTerm", "설명": "용어 삭제", "우선순위": "중"},
    {"모듈": "용어사전 관리", "하위 모듈": "용어 관리", "기능ID": "TM-105", "기능명": "importTerms", "설명": "용어 일괄 가져오기", "우선순위": "중"},
    {"모듈": "용어사전 관리", "하위 모듈": "용어 관리", "기능ID": "TM-106", "기능명": "exportTerms", "설명": "용어 내보내기", "우선순위": "중"}
]

# 모든 데이터 합치기
all_features = (
    user_management +
    permission_management +
    menu_management +
    llm_management +
    deployment_management +
    dictionary_management
)

# DataFrame 생성
df = pd.DataFrame(all_features)

# 우선순위별 정렬 (상 > 중 > 하)
priority_order = {'상': 0, '중': 1, '하': 2}
df['우선순위_정렬'] = df['우선순위'].map(priority_order)
df = df.sort_values(['모듈', '하위 모듈', '우선순위_정렬'])
df = df.drop('우선순위_정렬', axis=1)

# Excel 파일로 저장
with pd.ExcelWriter('hifenn_feature_priority.xlsx', engine='openpyxl') as writer:
    # 전체 기능 목록
    df.to_excel(writer, sheet_name='전체 기능 목록', index=False)
    
    # 우선순위별 시트
    for priority in ['상', '중', '하']:
        priority_df = df[df['우선순위'] == priority]
        priority_df.to_excel(writer, sheet_name=f'{priority}순위 기능', index=False)
    
    # 모듈별 시트
    for module in df['모듈'].unique():
        module_df = df[df['모듈'] == module]
        module_df.to_excel(writer, sheet_name=f'{module}', index=False)

print("Excel file has been created successfully!")