import React from 'react';
import { Admin, Resource, ListGuesser } from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';

const dataProvider = jsonServerProvider('http://127.0.0.1:8080');
const App = () => (
  <Admin dataProvider={dataProvider}>
    <Resource name='commands/' list={ListGuesser} />
  </Admin>
);

export default App;
