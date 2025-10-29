import type { ActionFunctionArgs } from "react-router";

export async function TubeAction({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const radius = formData.get('radius');
  const height = formData.get('height');

  // Simulate API call to backend
  const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      radius,
      height,
      formula: '2 * π * radius * (radius + height)',
    }),
  });

  if (!response.ok) {
    return { success: false, error: 'Failed to calculate' };
  }

  // Calculate surface area (2πr(r + h))
  const surfaceArea = 2 * Math.PI * Number(radius) * (Number(radius) + Number(height));

  return { success: true, result: parseFloat(surfaceArea.toFixed(2)) };
}

