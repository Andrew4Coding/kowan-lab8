import type { ActionFunctionArgs } from "react-router";

export async function SquareAction({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const side = formData.get('side');

  // Simulate API call to backend
  const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      side,
      formula: 'side * side',
    }),
  });

  if (!response.ok) {
    return { success: false, error: 'Failed to calculate' };
  }

  // Calculate area
  const area = Number(side) * Number(side);

  return { success: true, result: area };
}

