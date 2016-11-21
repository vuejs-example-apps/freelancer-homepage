import request from 'axios'

request.defaults.baseURL = 'http://localhost:8000/api/' // TODO: extract configuration to ENV

export const fetchSnapshot = ({ commit, state }) => {
  return request.get('snapshot.json').then((response) => {
    if (response.statusText === 'OK') {
      commit('SET_SNAPSHOT', response.data)
    }
  }).catch((error) => {
    console.log(error)
  })
}