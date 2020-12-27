// Contains a convenience method that we will be using to update the object properties.


export const updateObject = (oldObject, updatedProperties) => {
  return {
    ...oldObject,
    ...updatedProperties
  }
}