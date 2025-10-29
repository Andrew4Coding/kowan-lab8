import type { ActionFunctionArgs } from "react-router";

export async function CubeAction({ request }: ActionFunctionArgs) {
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
      formula: '6 * side * side',
    }),
  });

  if (!response.ok) {
    return { success: false, error: 'Failed to calculate' };
  }

  // Calculate surface area (6 * side^2)
  const surfaceArea = 6 * Number(side) * Number(side);

  return { success: true, result: surfaceArea };
}

