const { ApolloServer, gql } = require('apollo-server');

let persons = [
  {
    name: "Logan",
    phone: "312-1234789",
    alias: "Wolverine",
    city: "Cold Lake",
    power: "Claws",
    id: "w0lv3r1n3-63xm3n"
  },
  {
    name: "Scott",
    phone: "321-8597461",
    alias: "Cyclops",
    city: "Alkali Lake",
    power: "Optic blasts",
    id: "cyc10pt1c_63xm3n"
  },
  {
    name: "Jean",
    alias: "Phoenix",
    city: "Annandale-on-Hudson",
    power: "Telekinesis and telepathy",
    id: "ph03n1x-63xm3n"
  },
];

const typeDefinitions = gql`
  type Person {
    name: String!
    phone: String
    alias: String!
    city: String!
    power: String!
    id: ID!
  }

  type Query {
    personCount: Int!
    allPersons: [Person]!
    findPerson(name: String!): Person
  }

  type Mutation {
    addPerson(
      name: String!
      phone: String
      alias: String!
      city: String!
      power: String!
    ): Person
    updatePerson(
      id: ID!
      name: String
      phone: String
      alias: String
      city: String
      power: String
    ): Person
    deletePerson(
      id: ID!
    ): Person
  }
`;

const resolvers = {
  Query: {
    personCount: () => persons.length,
    allPersons: () => persons,
    findPerson: (root, args) => {
      const { name } = args;
      return persons.find(person => person.name === name);
    }
  },
  Mutation: {
    addPerson: (root, args) => {
      const newPerson = { ...args, id: Math.random().toString(36).substr(2, 9) };
      persons.push(newPerson);
      return newPerson;
    },
    updatePerson: (root, args) => {
      const { id, name, phone, alias, city, power } = args;
      const personIndex = persons.findIndex(person => person.id === id);
      if (personIndex === -1) {
        throw new Error("Persona no encontrada");
      }
      const updatedPerson = { ...persons[personIndex], name, phone, alias, city, power };
      persons[personIndex] = updatedPerson;
      return updatedPerson;
    },
    deletePerson: (root, args) => {
      const { id } = args;
      const personIndex = persons.findIndex(person => person.id === id);
      if (personIndex === -1) {
        throw new Error("Persona no encontrada");
      }
      const deletedPerson = persons.splice(personIndex, 1)[0];
      return deletedPerson;
    }
  }
};

const server = new ApolloServer({
  typeDefs: typeDefinitions,
  resolvers
});

server.listen().then(({ url }) => {
  console.log(`Servidor listo en ${url}`);
});
