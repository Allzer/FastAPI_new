import {Card} from 'antd'

function CardIndex() {

  return (
    <>
      <Card title="Карточка приколов" extra={<a href="#">More</a>} style={{ width: 300 }}>
        <p>Мем</p>
        <p>Прикол</p>
        <p>Шутка</p>
      </Card> 
    </>
  )
}

export default CardIndex
