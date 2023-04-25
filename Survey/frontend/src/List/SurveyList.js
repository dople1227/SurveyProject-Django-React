import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Pagination from '@mui/material/Pagination';
import SurveyListTable from './SurveyListTable';
import useFetchTable from '../hooks/useFetchTable';
import axios from 'axios';

function SurveyList() {
  const navigate = useNavigate();
  const [page, setPage] = useState(1);
  const { data, loading, error, totalPages } = useFetchTable(
    '"http://ec2-15-164-163-67.ap-northeast-2.compute.amazonaws.com:8000/api/survey',
    {},
    page,
  );

  // 페이지 이동시 실행
  const handleChangePage = (event, value) => {
    setPage(value);
  };

  // 수정하기 클릭 시 실행
  const handleClickModify = (e) => {
    const surveyId = e.target.dataset.surveyid;
    if (surveyId) {
      navigate(`/form/${surveyId}`);
    }
  };

  // 삭제하기 클릭 시 실행
  const handleClickDelete = async (e) => {
    //axios요청에 필요한 변수 SET
    const surveyId = e.target.dataset.surveyid;
    const url = `http://ec2-15-164-163-67.ap-northeast-2.compute.amazonaws.com:8000/api/survey/${surveyId}/`;
    // const url = `http://localhost:8000/api/survey/${surveyId}/`;
    const method = 'delete';
    const successMessage = '설문지가 삭제되었습니다.';

    // 백엔드로 전송할 데이터 SET
    const data = { surveyId: surveyId };

    // axios.delete 요청 실행
    try {
      await axios[method](url);
      alert(successMessage);
      window.location.reload();
    } catch (error) {
      console.error('API 요청 실패:', error);
    }
  };

  // 페이지 로딩 및 에러처리. 추후 컴포넌트로 분리해서 구현
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <SurveyListTable
        data={data}
        handleClickModify={handleClickModify}
        handleClickDelete={handleClickDelete}
      />
      <Pagination count={totalPages} page={page} onChange={handleChangePage} />
    </div>
  );
}

export default SurveyList;
