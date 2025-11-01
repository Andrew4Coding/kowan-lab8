import type { ActionFunctionArgs } from "react-router";

export async function TubeAction({ request }: ActionFunctionArgs) {
  const formData = await request.formData();
  const radius = formData.get('radius');
  const height = formData.get('height');

  // Call AWS API
  const response = await fetch('https://t7ow9idud3.execute-api.us-east-1.amazonaws.com/tube-cylinder-surface/calculate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      jari_jari: Number(radius),
      tinggi: Number(height),
    }),
  });

  if (!response.ok) {
    return { success: false, error: 'Failed to calculate' };
  }

  const data = await response.json();

  return { success: true, result: data.luas_selimut };
}

